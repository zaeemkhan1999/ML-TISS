// pages/api/upload.js
import multer from 'multer';
import path from 'path';
import { promisify } from 'util';
import fs from 'fs';

// Create the uploads directory if it doesn't exist
const mkdir = promisify(fs.mkdir);
const uploadDir = path.join(process.cwd(), 'uploads');

async function ensureUploadDir() {
  try {
    await mkdir(uploadDir);
  } catch (err) {
    if (err.code !== 'EEXIST') {
      throw err;
    }
  }
}

// Configure multer storage
const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    cb(null, Date.now() + path.extname(file.originalname));
  },
});

const upload = multer({ storage: storage });

export const config = {
  api: {
    bodyParser: false,
  },
};

const handler = async (req, res) => {
  await ensureUploadDir();

  upload.single('file')(req, res, (err) => {
    if (err instanceof multer.MulterError) {
      // A Multer error occurred when uploading.
      return res.status(500).json({ error: err.message });
    } else if (err) {
      // An unknown error occurred when uploading.
      return res.status(500).json({ error: err.message });
    }

    // Everything went fine.
    res.status(200).json({ data: 'File uploaded successfully' });
  });
};

export default handler;
