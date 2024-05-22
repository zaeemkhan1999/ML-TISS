import multer from 'multer';
import path from 'path';
import { promisify } from 'util';
import fs from 'fs';

const mkdir = promisify(fs.mkdir);
const uploadDir = path.resolve(process.cwd(), '../uploads');

async function ensureUploadDir() {
  try {
    await mkdir(uploadDir);
  } catch (err) {
    if (err.code !== 'EEXIST') {
      throw err;
    }
  }
}

const storage = multer.diskStorage({
  destination: function (req, file, cb) {
    cb(null, uploadDir);
  },
  filename: function (req, file, cb) {
    cb(null, 'data' + path.extname(file.originalname));
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
      return res.status(500).json({ error: err.message });
    } else if (err) {
      return res.status(500).json({ error: err.message });
    }

    res.status(200).json({ data: 'File uploaded successfully' });
  });
};

export default handler;
