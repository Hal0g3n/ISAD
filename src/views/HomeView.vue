<template>
  <hello-world />
</template>

<script lang="ts">
  import Vue from "vue";
  import HelloWorld from "../components/HelloWorld.vue";

  export default Vue.extend({
    name: "HomePage",

    components: {
      HelloWorld,
    },
  });
</script>
