<template>
    <div class = "CDT">
        <h1 class="subheading grey--text">CDT</h1>

        <v-file-input 
         @change="Preview_image"
         v-model="image"/>


        <v-img :src="url"></v-img>
    </div>
</template>



<script>

import Vue from "vue";

export default Vue.extend({
    name: "HomePage",
    data: () => ({count: 0}),
    methods: {
        Preview_image(e) {
            if (e) {
                $("#image_id").attr("src", URL.createObjectURL(e)); // jQuery selector
            }
        }
    }
});

</script>
