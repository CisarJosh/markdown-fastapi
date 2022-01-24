<template>
  <div class="relative bg-white">
    <div class="absolute inset-0" aria-hidden="true">
      <div class="absolute inset-y-0 right-0 w-1/2"></div>
    </div>
    <div class="relative max-w-7xl mx-auto lg:px-8 lg:grid lg:grid-cols-2">
      <div class="bg-white py-16 px-4 sm:py-24 sm:px-6 lg:px-0 lg:pr-8">
        <div class="max-w-lg mx-auto lg:mx-0">
          <h2
            class="text-base font-semibold tracking-wide text-indigo-600 uppercase"
          >
            Markdown Converter
          </h2>
          <label for="markdown" class="block text-sm font-medium text-gray-700"
            >Enter Markdown</label
          >
          <form action="#" method="POST">
            <div class="mt-1">
              <textarea
                id="markdown"
                v-model="md"
                rows="10"
                name="markdown"
                class="shadow-sm focus:ring-indigo-500 focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md"
              ></textarea>
              <button
                type="submit"
                class="inline-flex items-center mt-5 px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                @click.prevent="submit"
              >
                Update
              </button>
            </div>
          </form>
        </div>
      </div>
      <div
        class="py-16 px-4 sm:py-24 sm:px-6 lg:bg-none lg:px-0 lg:pl-8 lg:flex lg:items-center lg:justify-end"
      >
        <div
          class="mt-12 relative text-base max-w-prose mx-auto lg:mt-0 lg:max-w-none"
        >
          <article class="prose lg:prose-xl">
            <div id="app" v-html="markup" />
          </article>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import { Action, Component, Getter, Prop, Vue } from "nuxt-property-decorator"
import { markdownMarkup } from "@/interfaces"

@Component({
  middleware: "anonymous",
})
export default class markdownToMarkup extends Vue {
  @Action("main/convertMarkdown") convertMarkdown
  @Prop({ required: false, type: String, default: "Add your markup here" })
  md!: string
  public async submit() {
    const markdown: markdownMarkup = { data: this.md }

    await this.convertMarkdown(markdown)
  }

  @Getter("main/markup") markup
}
</script>
