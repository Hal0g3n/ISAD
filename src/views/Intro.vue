<template>
    <div class = "Intro">
        <h1 class="subheading grey--text">Test</h1>

        <v-btn @click="onClick"/>


        <v-img :src="url"></v-img>
    </div>
</template>



<script>

import Vue from "vue";

export default Vue.extend({
    name: "HomePage",
    data: () => ({count: 0}),
    methods: {
        onClick() {
            this.$emit("complete", "CDT");
        }
    }
});

</script>
