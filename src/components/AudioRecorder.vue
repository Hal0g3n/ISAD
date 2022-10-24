<template>
    <button class="AudioRecorder" @click="click" :disabled="recordingEndedAt!=null">
        
        <v-btn v-if="!isRecording" :disabled="recordingEndedAt!=null" x-large class="red" fab>
            <v-icon color=white x-large>mdi-microphone</v-icon>
        </v-btn>
        
        <v-btn v-else x-large class="red" color='white' dark rounded>
            {{ time_remaining }}s
        </v-btn>

    </button>    
</template>

<script>
import Recorder from "recorder-js";

const DEFAULT_OPTIONS = { sampleRate: 44100, bufferSize: 16384 };

export default {
    data: () => ({
        isRecording: false,
        time_remaining: 60,
        recordingStartedAt: null,
        recordingEndedAt: null,
        recorder: null,
        audioContext: null,
        strema: null,
        recorderOptions: DEFAULT_OPTIONS
    }),

    async mounted() {
        await this.initiatePlayer().catch((err) => {
            console.error("Audio Recorder Error");
            this.$emit("error", error);
            throw error;
        });
    },

    methods: {
        updater: false,
        async initiatePlayer() { // Initializes the player
            this.audioContext = new (window.AudioContext ||
                window.webkitAudioContext)();

            this.isInitiated = true;
            this.$emit("initiated");
        },

        async click() {
            if (!this.isRecording) { // Start recording
                this.stream = await navigator.mediaDevices.getUserMedia({
                    audio: true
                });

                this.recorder = new Recorder(this.audioContext, this.recorderOptions);
                this.recorder.init(this.stream);
                
                await this.recorder.start();
                
                this.recordingStartedAt = performance.now();

                this.time_remaining = 60;
                this.isRecording = true;
                this.updater = setInterval(()=>{
                    this.time_remaining = 60000 - performance.now() + this.recordingStartedAt;
                    this.time_remaining = Math.ceil(this.time_remaining / 1000);
                    
                    if (this.time_remaining > 0) return;

                    this.click();
                }, 500);
            } 

            else { // Stop Recording
                this.recordingEndedAt = performance.now();

                const tracks = this.stream.getTracks();
                
                tracks.forEach((track) => {
                    track.stop();
                });

                const { blob } = await this.recorder.stop();

                this.$emit("result", {
                    blob: blob,
                    duration: this.recordingEndedAt - this.recordingStartedAt,
                    type: blob.type
                });

                
                // Stops the Timer
                clearInterval(this.updater);

                // No longer Recording
                this.isRecording = false;
            }
            console.log(this.isRecording);
        }
    }
};
</script>