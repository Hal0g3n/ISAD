<template>
    <div class = "Intro"> <center>

        <img class=ma-10 style="height:50vmin; width=50vmin" src="@/assets/logo.svg"/>
        
        <p class="text-h6">
            Intelligent Screening for Alzheimer's Disease. 
            A simple 10 minute test to check for Alzheimer's.<br>
            A project by Vikram Ramanathan, James Sng and Yap Yuan Xi
        </p>

        <v-btn class=primary @click="()=>this.$emit('complete', 'Memory')">Take the Test</v-btn>

    </center></div>
</template>



<script>
import Vue from "vue";

export default Vue.extend({
    data: () => ({count: 0}),
});

</script>
