document.addEventListener("DOMContentLoaded", function() {
    // Initialize Dropzone
    Dropzone.options.uploadForm = {
        paramName: "photo",
        maxFilesize: 5, // in MB
        acceptedFiles: "image/*",
        dictDefaultMessage: "Drag & Drop or Click to Upload",
        init: function() {
            this.on("success", function(file, response) {
                // Handle successful upload, e.g., display a success message
                alert("Photo uploaded successfully!");
            });
        }
    };
});
