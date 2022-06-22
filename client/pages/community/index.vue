
<template>
  <main class="container mt-5">
    <div class="row">
      <div class="col-12 text-right mb-4">
        <div class="d-flex justify-content-between">
          <h3>La Communities</h3>
          <nuxt-link to="/community/add" class="btn btn-info">Add Community</nuxt-link>
        </div>
      </div>
      <template v-for="community in communities">
        <div :key="community.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
          <community-table :onDelete="deleteCommunity" :community="community"></community-table>
        </div>
      </template>
    </div>
  </main>
</template>

<script>
import CommunityTable from "~/components/CommunityTable.vue";

export default {
  head() {
    return {
      title: "Communities list"
    };
  },
  components: {
    CommunityTable
  },
  async asyncData({ $axios, params }) {
    try {
      const communities = await $axios.$get(`/community/`);
      return { communities };
    } catch (e) {
      return { communities: [] };
    }
  },
  data() {
    return {
      communities: []
    };
  },
  methods: {
    async deleteCommunity(community_id) {
      try {
        await this.$axios.$delete(`/community/${community_id}/`); // delete community
        const newCommunity = await this.$axios.$get("/community/"); // get new list of communities
        this.communities = newCommunity; // update list of communities
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>

<style scoped>
</style>
