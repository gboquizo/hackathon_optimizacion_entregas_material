export default class Manager {
  constructor () {
    this.loadEvents()
  }

  loadEvents () {
    this.download()
    this.destroy()
  }

  download () {
    $('.download').click(function () {
      window.location = '/files/download/' + $(this).data('filename')
    })
  }

  destroy () {
    const _this = this
    $('.delete').click(function () {
      Swal.fire(_this.preventSwalObject()).then((result) => { if (result.value) { _this.deleteCall($(this)) } })
    })
  }

  preventSwalObject() {
    return {
      title: 'Are you sure?',
      text: "You won't be able to revert this!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#9c27b0',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Yes, delete it!'
    }
  }

  deleteCall(el) {
    axios.delete('/files/delete/' + el.data('id'))
      .then(response => {
        if (response.data.success) {
          Swal.fire({
            position: 'top-end',
            icon: 'success',
            title: response.data.message,
            showConfirmButton: false,
            timer: 1500
          })
          this.removeParent(el)
        }
      })
  }

  removeParent (el) {
    if ($('.table > tbody > tr').length === 1) {
      $('.table > tbody').append("<th scope='row' colspan='5' class='text-center'>There is no files</th>")
    }
    el.parent().parent().remove()
  }
}
