<template>
  <div class="Results">
    <h1 class="subheading grey--text">Results</h1>


    <v-container class=my-5>
        <v-row justify="space-around">
            <vue-ellipse-progress 
                animation="default 2500 0"
                align = 'center'
                :progress="cdt"/>
            <vue-ellipse-progress 
                animation="default 2500 3000"
                align = 'center'
                :progress="cvft"/>
            <vue-ellipse-progress 
                animation="default 2500 5500"
                align = 'center'
                :progress="mcog"/>
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
        cdt: api.cdt,
        cvft: api.cvft,
        mcog: api.mcog
    }),

    components: {VueEllipseProgress},
});
</script>