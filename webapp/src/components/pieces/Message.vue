<template>
  <div class="alert alert-{{ tag }}">
    <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
    </button>
    <b v-show="title">{{ title }} : </b> {{ message }}
  </div>
</template>

<script>
export default {
  props: [
    'tag',
    'title',
    'message'
  ]
};
</script>

<style scope>
  .alert {
    margin-top: 50px;
  }
</style>
