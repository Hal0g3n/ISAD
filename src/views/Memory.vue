<template>
    <div class = "Memory">
        <v-container>
            <h1>Memory</h1>
            
            <div v-if="!seen">
                Memorise the words below
                <li v-for="word in data.words" :key="word">
                    {{ word }}
                </li>
                <v-btn class="primary" style="margin-top:3vmin" @click="seen = true;$emit('complete')">Done!</v-btn>
            </div>


        </v-container>
    </div>
</template>

<script lang="ts">
import Vue from "vue";
import { data } from "@/model/Data";

export default Vue.extend({
    data: () => ({
        data,
        seen: false
    }),
});

</script>