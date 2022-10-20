<template>
    <div class = "Memory">
        <v-container>
            <h1>Memorise these words</h1>
            
            <div v-if="!seen">
                <li v-for="word in data.words" :key="word">
                    {{ word }}
                </li>
                <v-btn class="primary" style="margin-top:3vmin" @click="seen = true;$emit('complete')">Done!</v-btn>
            </div>

            <div v-else>
                <img src="https://i.imgflip.com/13044w.jpg"/>
                No Cheating! <v-btn style="margin-left: 1vw" class=primary @click="$emit('complete')">OK FINE</v-btn>
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