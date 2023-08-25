function confirmDelete() {
    return window.confirm("Are you sure you want to delete this post?");
}

function confirmDeleteComment() {
    return window.confirm("Are you sure you want to delete this comment?");
}

function closeCommentSuccessAlert() {
    const commentSuccessAlert = document.getElementById('comment-success-alert');
    commentSuccessAlert.style.display = 'none';
}


function handleCommentSubmission() {
    const commentSuccessAlert = document.getElementById('comment-success-alert');
    commentSuccessAlert.style.display = 'block';
}