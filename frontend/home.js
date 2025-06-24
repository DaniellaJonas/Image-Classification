function upload(){
    document.getElementById('fileInput').click();
    console.log("It's working")
}

function img_load(event){
   const file = event.target.files[0];
    if (!file || (file.type !== "image/jpeg" && file.type !== "image/png")) {
        return;
    } 
    const img = document.getElementById("preview");
    img.src = URL.createObjectURL(file);  
    img.onload = () => {
        URL.revokeObjectURL(img.src); 
    }
}

