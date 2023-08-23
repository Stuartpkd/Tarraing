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

document.getElementById('upload-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const form = event.target;
    const formData = new FormData(form);

    try {
        const response = await fetch(form.action, {
            method: 'POST',
            body: formData
        });

        if (response.ok) {
            const data = await response.json();
            if (data.error) {
                const modal = new bootstrap.Modal(document.getElementById('error-modal'));
                const modalBody = document.querySelector('#error-modal .modal-body');
                modalBody.textContent = data.error;
                modal.show();
            }
        }
    } catch (error) {
        console.error('Error:', error);
    }
});


function closeCommentSuccessAlert() {
    const commentSuccessAlert = document.getElementById('comment-success-alert');
    commentSuccessAlert.style.display = 'none';
}


function handleCommentSubmission() {
    const commentSuccessAlert = document.getElementById('comment-success-alert');
    commentSuccessAlert.style.display = 'block';
}