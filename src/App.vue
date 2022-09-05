<template>
    <v-app class="grey lighten-4">
        <transition name="fade" mode="out-in"> <!-- Animate in when doing test -->
            <ProgressBar
                style="align: center;"
                :steps="steps"
                :active-step="step"
                :highestStep="5"
                reactivityType="all"
                :isReactive="true"
                :showBridge="true"
                :showLabel="false"
                class = 'mx-4'
                v-if="!isHome"
                @onStepChanged="onStepChanged"/>
        </transition>

        <!-- Transitions for my views -->
        <transition :name="anim" mode='out-in'>
            <keep-alive> <!-- Forces the state of routes to save -->
                <router-view class = 'mx-4 mb-4' @complete="unlockStep"/>
            </keep-alive>
        </transition>

    </v-app>
</template>



<script lang="ts">
import Vue from "vue";
import ProgressBar from "@/components/ProgressBar.vue";

// Route to Steps
const steps: string[] = [
    "Memory", 
    "CDT",
    "Recall", 
    "CVFT",
    "Results"
];

export default Vue.extend({
    name: "App",
    components: {ProgressBar},
    data: () => ({
        step: -1,
        highestStep: -1,
        steps,
        anim: "fade",
        isHome: true
    }),

    created() {
        // Forces users to enters in correct route
        if (this.$route.name != "Homepage") this.$router.push("/");
    },

    watch: { // Observer for route changes

        $route (to) { // Changes Progress bar accordingly

            // What is the next index position
            var next: number = steps.indexOf(to.name);

            // Handles Animation Slide Direction
            if (next < this.step) this.anim = "slider-left";
            else this.anim = "slider-right";

            // Time delay to make animation nicer
            setTimeout(() => this.isHome = to.name == "Homepage", to.name == "Homepage" ? 0 : 350);

            // Set step to next step
            this.step = next;
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
            // Sets highest step reachable
            this.highestStep = Math.max(steps.indexOf(step), this.highestStep);

            // Reroute to expected step
            this.onStepChanged(steps.indexOf(step));
        },
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



.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.5s ease-out;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>
