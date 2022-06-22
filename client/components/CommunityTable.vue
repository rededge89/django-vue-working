
<template>
  <div class="card community-table">
    <div class="card-body">
      <h5 class="card-title">{{ community.name }}</h5>
      <p class="card-text">
        <strong>Ingredients:</strong> {{ community.ingredients }}
      </p>
      <div class="action-buttons">
        <nuxt-link :to="`/recipes/${community.id}/`" class="btn btn-sm btn-success"> View </nuxt-link>
        <nuxt-link :to="`/recipes/${community.id}/edit/`" class="btn btn-sm btn-primary"> Edit </nuxt-link>
        <button class="btn btn-sm btn-danger"  @click="onDelete(community.id)">Delete</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {
    props: ["community", "onDelete"]
};
</script>
<style>
.community-table {
    box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
}
</style>
