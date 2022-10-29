<template>
  <div class="Results">

    <v-container>
        
        <v-row justify="center">
            <vue-ellipse-progress 
                v-for="(score, name) in data.scores" :key="name"
                class='mx-auto my-5'
                animation="default 2000 0"
                emptyColor="#fcfff7"
                :size="250"
                :thickness="15"
                emptyThickness="10%"
                fontSize="5rem"
                :color="rgbToHex((100 - score) * 2.55, score * 2.55, 0)"
                :progress="Math.round(score)"
                :loading="score==-1">
                <template>
                    <span slot='legend-value'>%</span>
                    <span slot='legend-caption'>{{ name }}</span>
                </template>
            </vue-ellipse-progress>
        </v-row>
        
        <center class="text-h4 my-10">
            Find out more about Dementia and Alzheimer's <a href="https://www.dementiahub.sg/">here</a>
        </center>

        <div v-if="loaded">
            <center class="text-h3">You passed {{passed}} of {{tests.length}} tests</center>
            <center class="text-h4 my-1 mb-5">{{ message }}</center>

            <div v-if="passed < tests.length" style="margin: 0 max(0px, calc(100vw - 70rem)); border: 1vmin solid black">
                <center class="text-h6">Consider calling the hotlines below</center>

                <div class=ma-1 style="font-size:1.15rem;">
                    Dementia Singapore: 6377 0700               <br>
                    AIC Hotline: 1800-650-6060                  <br>
                    Health Promotion Board: 1800-223-1313 <br>
                </div>
            </div>
        </div>

    </v-container>

  </div>
</template>

<script lang="ts">
import Vue from "vue";
import { data } from "@/model/Data";
import { VueEllipseProgress } from "vue-ellipse-progress";


var hexRange: string[] = [];
const digits = "0123456789abcdef".split("");
digits.forEach((outer) => {
    digits.forEach((inner) => {
        hexRange.push(outer + inner);
    });
});


export default Vue.extend({
    data: () => ({
        data,
        tests: Object.keys(data.scores)
    }),

    methods: {
        rgbToHex(...vals: number[]) {
            //Split up the RGB(A) string on commas and match numbers
            let invalid = false;

            //Make sure none of the numbers are larger than 255
            vals.forEach((val) => {
                if (val > 255 || val < 0) invalid = true;
            });

            if (invalid) return "#caabff";

            //Make sure we have 3 or 4 numbers (RGB or RGBA)
            if ([3, 4].includes(vals.length)) {
                let finalHex = "";
                vals.forEach((color) => {
                    //If we're dealing with the alpha value…
                    color = Math.ceil(color);

                    hexRange.forEach((hex, hexIndex) => {
                        if (color == hexIndex) finalHex += hex;
                    });

                });
                return `#${finalHex}8f`;
            }
        }
    },

    computed: {
        passed() {
            var count = 0;

            for (var test in data.scores) 
                count += (data.scores[test] >= 50) ? 1 : 0;

            return count;
        },

        loaded() {
            
            for (var test in data.scores) 
                if (data.scores[test] == -1) return false;

            return true;
        },

        message() {
            var percent = this.passed / this.tests.length * 100;
            if (percent >= 80) return "You probably do not have Alzheimer's";
            else if (percent >= 50) return "You might not have Alzheimer's";
            else if (percent >= 20) return "You might have Alzheimer's";
            else return "You most likely have Alzheimer's";
        }
    },

    components: {VueEllipseProgress},
});
</script>