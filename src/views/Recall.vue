<template>
  <div class="Recall">
    <v-container class=my-5 fill-height>
        <v-row><h1 class="subheading grey--text">Recall Test</h1></v-row>

        <v-row><div>Type out the 3 words you memorised just now</div></v-row>

        <v-row v-for="(word, index) in recalled" :key="word">
            <v-col cols=10><v-text-field v-model="word.value" :key="index"/></v-col>
        </v-row>
        <v-btn class="primary" style="margin-top:3vmin" @click="click">Submit</v-btn>
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
