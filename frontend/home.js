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

    img.onload = () => { // טוענת תמונה
        URL.revokeObjectURL(img.src); 
        // מוחקת תמונה מהזיכרון
        img.style.display = "block";
        // מציגה אותה בפרונטאנד

    };


    // יוצרת תיקייה לתמונה
    const formData = new FormData();
    formData.append("file", file);


    // שולחים לפלסק את התמונה לבדיקה
    fetch("http://localhost:5000/predict", { 
        method: "POST",
        body: formData
    })

    // מקבל תשובה ואם שגיאה מחזיר שגיאה
    .then(response => {
        if (!response.ok) {
            // throw new Error("HTTP status " + response.status)
            alert("Error");
        }
        return response.text();
    })

    // מדפיס תשובה של הדאטה
    .then(data => {
        alert("Prediction: " + data);
    })

    //בודקים איזה שגיאה התקבלה מthen
    .catch(error => {
        console.error("Error:", error);
        alert("Something went wrong: " + error.message);
    });
}
