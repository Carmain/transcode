<template>
  <div class="alert alert-{{ tag }}">
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
    {{ message }}
  </div>
</template>

<script>
export default {
  props: [
    'message'
    'tag'
  ]
}
</script>

<style scope>
  .alert {
    margin-top: 50px;
  }
</style>
