import FileUpload from "@/components/FileUpload";
import Head from "next/head";

export default function Home() {
  return (
    <div className="bg-custom-gradient h-[100vh] flex items-center justify-center">
      <Head>
        <title>Secure File Upload</title>
      </Head>

      <div className="bg-innerbox-gradient w-[50%] h-[70%] flex flex-col gap-5 items-center justify-center rounded-lg">
        <h2 className="text-4xl">ML - TISS</h2>
        <div className="">
          <FileUpload />
        </div>
      </div>
    </div>
  );
}
