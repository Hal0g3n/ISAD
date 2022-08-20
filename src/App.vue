<template>
    <v-app class="grey lighten-4">
        <ProgressBar
            :v-show="false"
            :steps="steps"
            :active-step="step"
            :highestStep="highestStep"
            reactivityType="backward"
            :is-reactive="true"
            :showBridge="true"
            :showLabel="false"
            class = 'mx-4'
            @onStepChanged="onStepChanged"/>

        <!-- Transitions for my views -->
        <transition :name="'slider-' + anim_dir" mode='out-in'>
            <keep-alive> <!-- Forces the state of routes to save -->
                <router-view class = 'mx-4 mb-4' @complete="unlockStep"/>
            </keep-alive>
        </transition>

    </v-app>
</template>



<script lang="ts">
import Vue from "vue";
import ProgressBar from "@/components/ProgressBar.vue";

// Setting Website Name
document.title = "ISAD";

// Route to Steps
const steps: string[] = [
    "CDT",  
    "MMSE", 
    "CVFT",
    "Results",
];

export default Vue.extend({
    name: "App",
    components: {ProgressBar},
    data: () => ({
        step: 0,
        highestStep: 0,
        steps,
        anim_dir: "right"
    }),

    created() {
        // Forces users to enters in correct route
        if (this.$route.name != "CDT") this.$router.push("/");
    },

    watch: { // Observer for route changes

        $route (to, from) { // Changes Progress bar accordingly

            // What is the next index position
            var next: number = steps.indexOf(to.name);
            console.log(to.name);

            // Handles Animation Slide Direction
            if (next < this.step) this.anim_dir = "left";
            else this.anim_dir = "right";

            this.step = next;
            console.log(this.step);
        }
    },

    // define methods under the `methods` object
    methods: {
        onStepChanged(step: number) {
            // If actually clicked on something different
            // Change the route
            if (step != this.step)
                this.$router.push("/" + steps[step]);
        },

        unlockStep(step: string) {
            if (steps.indexOf(step) > this.highestStep) {
                this.highestStep = steps.indexOf(step);
                this.onStepChanged(this.highestStep);
            }
        }
    }
});
</script>



<!-- Slide left & right animations -->
<style>
.slider-right-enter {
  opacity: 0;
  transform: translatex(100%);
}

.slider-right-enter-to {
    opacity: 1;
    transition: all 0.35s ease-out;
}

.slider-right-leave-to {
    opacity: 0;
    transform: translatex(-100%);
    transition: all 0.35s ease-out;
}

.slider-left-enter {
    opacity: 0;
    transform: translatex(-100%);
}

.slider-left-enter-to {
    opacity: 1;
    transition: all 0.35s ease-out;
}

.slider-left-leave-to {
    opacity: 0;
    transform: translatex(100%);
    transition: all 0.35s ease-out;
}
</style>
