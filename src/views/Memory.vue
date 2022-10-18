<template>
    <div class = "Memory">
        <v-container>
            <h1>Memorise these words</h1>
            
            <li v-for="word in api.words" :key="word">
                {{ word }}
            </li>
            <v-btn class="primary" style="margin-top:3vmin" @click="$emit('complete')">Done!</v-btn>

        </v-container>
    </div>
</template>

<script lang="ts">
import Vue from "vue";
import { API } from "@/model/Data";

export default Vue.extend({
    data: () => ({
        api: API.getInstance(),
    }),
});

</script>