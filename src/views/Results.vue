<template>
  <div class="Results">
    <h1 class="subheading grey--text">Results</h1>

    <v-container class=my-5>
        <v-row justify="space-around">
            <vue-ellipse-progress 
                animation="default 2000 0"
                align = 'center'
                color="#8fce00"
                emptyColor="#FFF07F"
                :size="300"
                :thickness="30"
                emptyThickness="15%"
                fontsize="100%"
                :progress="cdt">
                <template>
                    <span slot='legend-value'>%</span>
                    <span slot='legend-caption'>Drawing Test</span>
                </template>
            </vue-ellipse-progress>

            <vue-ellipse-progress 
                animation="default 2000 2500"
                align = 'center'
                color="#8fce00"
                emptyColor="#FFF07F"
                :size="300"
                :thickness="30"
                emptyThickness="15%"
                fontsize="100%"
                :progress="mcog">
                <template>
                    <span slot='legend-value'>%</span>
                    <span slot='legend-caption'>Recall Test</span>
                </template>
            </vue-ellipse-progress>

            <vue-ellipse-progress 
                animation="default 2000 5000"
                align = 'center'
                color="#8fce00"
                emptyColor="#FFF07F"
                :size="300"
                :thickness="30"
                emptyThickness="15%"
                fontsize="100%"
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