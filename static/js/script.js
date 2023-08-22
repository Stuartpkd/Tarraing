document.addEventListener("DOMContentLoaded", function () {
    let savedArtworkBtn = document.getElementById("artwork-btn");
    let postsBtn = document.getElementById("post-btn");
    let posts = document.getElementById("post-list");
    let savedArtworks = document.getElementById("saved-artwork-list");

    savedArtworkBtn.addEventListener("click", displayArtworks);
    postsBtn.addEventListener("click", displayPosts);

    function displayArtworks() {
        if (savedArtworks.classList.contains('hide')) {
            savedArtworks.classList.remove("hide");
            posts.classList.add('hide');
        }
    }

    function displayPosts() {
        if (posts.classList.contains('hide')) {
            posts.classList.remove('hide');
            savedArtworks.classList.add('hide');
        }
    }
});


function confirmDelete() {
    return confirm("Are you sure you want to delete this post?");
}


setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);


document.getElementById('upload-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);


    const fileInput = form.querySelector('input[type="file"]');
    if (fileInput.files.length > 0 && fileInput.files[0].size > 1024 * 1024) {
        const alertBox = document.getElementById('warning-alert');
        alertBox.style.display = 'block';
        return;
    }

    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData
        });

        if (response.ok) {

            window.location.href = response.url;
            const data = await response.json();
            if (data.error) {

                alert(data.error);
            }
        }
    } catch (error) {
        console.error('Error:', error);
    }
});