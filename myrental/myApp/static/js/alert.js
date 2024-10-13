document.addEventListener('DOMContentLoaded', function () {
  const deleteLinks = document.querySelectorAll('.delete-link');

  deleteLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault(); // Prevent the default link action

      const deleteUrl = this.getAttribute('href'); // Get the URL from the link

      // Show SweetAlert confirmation dialog
      Swal.fire({
        title: "Are you sure?",
        text: "You won't be able to revert this!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
      }).then((result) => {
        if (result.isConfirmed) {
          // If confirmed, redirect to the delete URL
          window.location.href = deleteUrl;

          // Optionally, you can show a success message after redirection
         
        }
      });
    });
  });
});
