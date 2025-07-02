function upload() {
  document.getElementById('fileInput').click();
}

function img_load(event) {
  const file = event.target.files[0];

  if (!file || (file.type !== "image/jpeg" && file.type !== "image/png")) {
    alert("Please upload a PNG or JPG image.");
    return;
  }

  const img = document.getElementById("preview");
  img.src = URL.createObjectURL(file);
  img.style.display = "block";

  img.onload = () => {
    URL.revokeObjectURL(img.src);
  };

  const formData = new FormData();
  formData.append("file", file);

  // שולח לפלסק
  fetch("http://localhost:5000/predict", {
    method: "POST",
    body: formData
  })
  .then(response => {
    if (!response.ok) throw new Error("HTTP status " + response.status);
    return response.text();
  })
  .then(data => {
    // מציג את התוצאה ב־HTML
    document.getElementById("result").innerText = "Prediction: " + data;
  })
  .catch(error => {
    console.error("Error:", error);
    document.getElementById("result").innerText = "Error: " + error.message;
  });
}
