<template>    
    <div class="Selection">
        <v-container>
            <h1>Test Selection</h1>
            
            <div v-for="test in api.tests" :key="test">
                <v-btn style="margin:2vh 0"
                    block
                    depressed
                    outlined
                    raised
                    rounded
                    text
                    @click="api.steps=test.steps; $emit('selected')">
                    {{ test.name }}
                </v-btn>
            </div>
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