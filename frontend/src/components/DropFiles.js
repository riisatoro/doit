import React, { useState } from 'react';
import {useDropzone} from 'react-dropzone';
import '../styles/dropfiles.css';

const DropFiles = ({ setIsApplying }) => {
    const {acceptedFiles, getRootProps, getInputProps} = useDropzone();
    const [isUploading, setIsUploading] = useState(false);

    const files = acceptedFiles.map((file) => (
        <span key={file.path} className="">
            {file.path},
        </span>
    ))

    return (
    <section className="drop-wrapper">
        <i className="fa-solid fa-3x fa-xmark text-right" onClick={() => setIsApplying(false)}></i>
        <div {...getRootProps({className: 'dropzone'})} className="drop-zone">
            <input {...getInputProps()} />
            {isUploading ? 
            <p>Files uploading, please wait...</p>
            : (
                <p className='drop-zone-text'>
                    Drag 'n' drop some files here, or click to select files
                    <i className="mx-1 fa-solid fa-photo-film"></i>
                    <hr />
                    {files && <p>Files to upload: {files}</p>}
                </p>
            )

            }
        </div>
    </section>
  );
}

export default DropFiles;
