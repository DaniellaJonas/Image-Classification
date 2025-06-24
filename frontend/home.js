function upload(){
    document.getElementById('fileInput').click();
    console.log("It's working")
}

function img_load(event){
   const file = event.target.files[0];
    if (!file || (file.type !== "image/jpeg" && file.type !== "image/png")) {
        console.log("Not image"),
        alert("Upload a PNG/JPG")
        return;
    } 
    const img = document.getElementById("preview");
    img.src = URL.createObjectURL(file);  
    img.onload = () => {
        URL.revokeObjectURL(img.src); 
        img.style.display = "block";

    }
}

