<template>
    <div class = "Intro">
        <h1 class="subheading grey--text">Test</h1>
        
        <svg src="../src/assets/logo.svg"/>

        <v-btn @click="()=>this.$emit('complete', 'Memory')">Take the Test</v-btn>
    </div>
</template>



<script>
import Vue from "vue";

export default Vue.extend({
    data: () => ({count: 0}),
});

</script>
