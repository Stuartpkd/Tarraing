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