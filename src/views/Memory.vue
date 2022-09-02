<template>
    <div class="Memory">
        <h1 class="subheading grey--text">ISAD</h1>


        <v-container>
            <v-row>Remember these 3 words</v-row>
            <v-row v-for="word in words" :key="word">{{ word }}</v-row>
            <v-row><v-btn @click="click"/></v-row>
        </v-container>

    </div>
</template>

<script lang="ts">
import Vue from "vue";
import { API } from "@/model/Data";

const api = API.getInstance();

export default Vue.extend({
    data: () => ({"words": api.words}),

    methods: {
        click() {
            this.$emit("complete", "CDT");
        }
    }
});

</script>