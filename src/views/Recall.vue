<template>
  <div class="Recall">
    <h1 class="subheading grey--text">Do you remember?</h1>
    
    <v-container class=my-5>
        <v-row>
            <div>What are the words to remember?</div>
        </v-row>

        <v-row v-for="(word, index) in recalled" :key="word"><v-text-field v-model="word.value" :key="index"/></v-row>
        <v-btn @click="click"/>
    </v-container>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { API } from "@/model/Data";

const api = API.getInstance();

export default Vue.extend({
    data: () => ({
        words: api.words, 
        recalled: [{value: ""}]
    }),

    mounted() {
        this.recalled = [];
        for (var {} of this.words) 
            this.recalled.push({value: ""});
    },

    methods: {
        click() {
            for (var data of this.recalled) 
                console.log(data.value);
            
            this.$emit("complete", "CVFT");
        }
    }
});

</script>
