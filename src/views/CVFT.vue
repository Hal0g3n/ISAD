<template>
    <div class = "CDT"> <transition name=fade mode=out-in>

        <v-container v-if="!ready" key="Prep">
            <h1>Test Requirements</h1>
            For this test, you will require:
            <li>Audio Capture Device (e.g. Microphone)</li>
            <v-btn @click="()=>ready=true">Ready!</v-btn>
        </v-container>

        
        
        <v-container v-else key="CDT">
            <h1 class="subheading grey--text">Verbal Fluency Test</h1>

            Record 1 min of you saying unique animal names.

            <center>
                <audio-recorder
                    :attempts="1"
                    :time="1"
                    :after-recording="()=>this.$emit('complete','Results')"/>
            </center>

        </v-container>

    </transition> </div>
</template>



<script>
import Vue from "vue";
import { AudioRecorder } from "vue-audio-recorder";

export default Vue.extend({
    components: { AudioRecorder },

    data: () => ({
        ready: false,
    }),
});

</script>



<style scoped>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.25s ease-out;
}

.fade-enter,
.fade-leave-to {
  opacity: 0;
}
</style>