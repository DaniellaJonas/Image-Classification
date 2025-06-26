function upload(){
    document.getElementById('fileInput').click();
    console.log("It's working")
}

function img_load(event) {
    const file = event.target.files[0];

    if (!file || (file.type !== "image/jpeg" && file.type !== "image/png")) {
        console.log("Not image");
        alert("Upload a PNG or JPG image.");
        return;
    }

    const img = document.getElementById("preview");
    img.src = URL.createObjectURL(file);
    
    img.onload = () => {
        URL.revokeObjectURL(img.src);
        img.style.display = "block";
    };

    const formData = new FormData();
    formData.append("file", file);

    fetch("http://10.0.0.15:5000/predict", {
        method: "POST",
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        alert("Prediction: " + data);
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong.");
    });

}
