<template>
  <div class="Results">
    <!-- <center class="text-h3 ma-5">You passed {{this.passed}} of 3 tests</center> -->

    <v-container>
        
        <v-row justify="center">
            <vue-ellipse-progress 
                v-for="(score, name) in scores" :key="name"
                class='mx-auto my-5'
                animation="default 2000 0"
                emptyColor="#faf7ff"
                :size="250"
                :thickness="15"
                emptyThickness="10%"
                fontSize="5rem"
                :color="(score >= 50) ? '#8fce00' : '#ff3c3c'"
                :progress="Math.round(score)"
                :loading="score==-1">
                <template>
                    <span slot='legend-value'>%</span>
                    <span slot='legend-caption'>{{ name }}</span>
                </template>
            </vue-ellipse-progress>
        </v-row>

    </v-container>

  </div>
</template>

<script lang="ts">
import Vue, { toRefs } from "vue";
import { data } from "@/model/Data";
import { VueEllipseProgress } from "vue-ellipse-progress";

export default Vue.extend({
    setup: () => ({
        // Stupid Reactivity, I will actually kill you
        ...toRefs(data)
    }),

    components: {VueEllipseProgress},
});
</script>