<template>
  <div class="Results">
    <h1>Results</h1>

    <v-container>
        <v-row justify="center">
            <vue-ellipse-progress 
                class='mx-auto my-5'
                animation="default 2000 0"
                color="#8fce00"
                emptyColor="#FFF07F"
                :size="250"
                :thickness="15"
                emptyThickness="10%"
                fontSize="5rem"
                :progress="cdt">
                <template>
                    <span slot='legend-value'>%</span>
                    <span slot='legend-caption'>Drawing Test</span>
                </template>
            </vue-ellipse-progress>

            <vue-ellipse-progress 
                class='mx-auto my-5'
                animation="default 2000 2500"
                color="#8fce00"
                emptyColor="#FFF07F"
                :size="250"
                :thickness="15"
                emptyThickness="10%"
                fontSize="5rem"
                :progress="mcog">
                <template>
                    <span slot='legend-value'>%</span>
                    <span slot='legend-caption'>Recall Test</span>
                </template>
            </vue-ellipse-progress>

            <vue-ellipse-progress 
                class='mx-auto my-5'
                animation="default 2000 5000"
                color="#8fce00"
                emptyColor="#FFF07F"
                :size="250"
                :thickness="15"
                emptyThickness="10%"
                fontSize="5rem"
                :progress="cvft">
                <template>
                    <span slot='legend-value'>%</span>
                    <span slot='legend-caption'>Verbal Test</span>
                </template>
            </vue-ellipse-progress>
        </v-row>
    </v-container>

  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { API } from "@/model/Data";
import { VueEllipseProgress } from "vue-ellipse-progress";

const api = API.getInstance();

export default Vue.extend({
    data: () => ({
        cdt: Math.round(api.cdt),
        cvft: Math.round(api.cvft),
        mcog: Math.round(api.mcog)
    }),

    components: {VueEllipseProgress},
});
</script>