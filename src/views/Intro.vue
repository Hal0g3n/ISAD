<template>
    <div class = "Intro">
        <h1 class="subheading grey--text">Test</h1>
        
        <svg src="../src/assets/logo.svg"/>

        <v-btn @click="()=>this.$emit('complete', 'Memory')">Take the Test</v-btn>


        <v-img :src="url"></v-img>
    </div>
</template>



<script>

import Vue from "vue";

export default Vue.extend({
    name: "HomePage",
    data: () => ({count: 0}),
});

</script>
