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
            var indices: Set<number> = new Set<number>();
            for (var data of this.recalled)
                indices.add(api.words.indexOf(data.value.toLowerCase()));

            // One point per correct word, -1 is incorrect so must remove
            api.mcog = indices.size - (indices.has(-1) ? 1 : 0);

            // Convert to percentage
            api.mcog = api.mcog * 100 / api.words.length;

            this.$emit("complete", "CVFT");
        }
    }
});

</script>
