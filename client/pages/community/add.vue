<template>
  <main class="container my-5">
    <div class="row">
      <div class="col-12 text-center my-3">
        <h2 class="mb-3 display-4 text-uppercase">{{ community.name }}</h2>
      </div>
      <div class="col-md-4">
        <form @submit.prevent="submitCommunity">
          <div class="form-group">
            <label for>Community Name</label>
            <input type="text" class="form-control" v-model="community.name">
          </div>
          <div class="form-group">
            <label for>Payroll Code</label>
            <input v-model="community.payroll_code" type="text" class="form-control">
          </div>
          <button type="submit" class="btn btn-primary">Submit</button>
        </form>
      </div>
    </div>
  </main>
</template>
<script>
export default {
  head() {
    return {
      title: "Add Community"
    };
  },
  data() {
    return {
      community: {
        name: "",
        payroll_code: "",
        badge_prefix: "",
        new_development: Boolean,
        currently_supported: Boolean,
        address_1: "",
        address_2: "",
        city: "",
        state: "",
        zip_code: ""
      },
      preview: ""
    };
  },
  methods: {
    async submitCommunity() {
      const config = {
        headers: {"content-type": "multipart/form-data"}
      };
      const formData = new FormData();
      for (const data in this.community) {
        formData.append(data, this.community[data]);
      }
      try {
        let response = await this.$axios.$post("/community/", formData, config);
        this.$router.push("/community/");
      } catch (e) {
        console.log(e);
      }
    }
  }
};
</script>
<style scoped>
</style>
