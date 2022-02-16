import React, { useContext, useState } from 'react';
import {useDropzone} from 'react-dropzone';
import { SEND_MEDIA_APPROVE_URL } from '../constants/urls'
import _ from 'lodash';
import '../styles/dropfiles.css';
import { AuthContext } from '../context/AuthContext';

const DropFiles = ({ setIsApplying, slug }) => {
    // const {acceptedFiles, getRootProps, getInputProps} = useDropzone();
    const [files, setFiles] = useState([]);
    const { apiInstance } = useContext(AuthContext);
    const [isUploading, setIsUploading] = useState(false);
    const {getRootProps, getInputProps} = useDropzone({
        accept: ['image/*', 'video/*'],
        onDrop: acceptedFiles => {
        setFiles(acceptedFiles.map(file => Object.assign(file, {
            preview: URL.createObjectURL(file)
        })).slice(0, 2));
        }
    });

    const sendMedia = () => {
        const formData = new FormData();
        files.slice(0, 2).forEach((file) => {
            formData.append('file', file)
        })
        apiInstance.post(SEND_MEDIA_APPROVE_URL(slug), formData)
        .then((response) => {
            setIsUploading(false);
            console.log(response)
        })
        .catch((error) => {
            setIsUploading(false);
            console.log(error)
        })
    }

    const filesPreview = files.map((file) => {
        if (file.type.includes('image')){
            return <img class='apply-media-preview' width='300px' height='300px' alt={file.path} src={file.preview} style={{objectFit: 'contain'}} />
        }
        return <iframe class='apply-media-preview' width='300px' height='300px' src={file.preview} title={file.path} />
    })

    return (
    <section className="drop-wrapper">
        <i className="fa-solid fa-3x fa-xmark text-right" onClick={() => setIsApplying(false)}></i>
        <div {...getRootProps({className: 'dropzone'})} className="drop-zone">
            <input name='file' {...getInputProps()} />
            {isUploading ? 
            <p>Files uploading, please wait...</p>
            : (
                <p className='drop-zone-text'>
                    Drag 'n' drop 2 files max here, or click to select files
                    <i className="mx-1 fa-solid fa-photo-film"></i>
                    <hr />
                    {!_.isEmpty(files) && <p>Files to upload: {filesPreview}</p>}
                </p>
            )
            }
        </div>
        {!_.isEmpty(files) && <button class='btn btn-primary' onClick={sendMedia}>Send media confirmation</button>}
    </section>
  );
}

export default DropFiles;
