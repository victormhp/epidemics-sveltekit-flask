<script lang="ts">
	import Icon from '@iconify/svelte';
	import { formatFileSize } from '$lib/utils';

	export let id: string;
	export let name: string;
	export let required = false;
	export let allowedExtensions = '*';
	export let files: FileList | undefined = undefined;
</script>

<div class="flex flex-col items-center justify-center w-full">
	<label
		for="dropzone-{id}"
		class="flex flex-col items-center justify-center w-full h-64 border-2 border-border border-dashed rounded-lg cursor-pointer bg-muted hover:bg-muted/50 transition-colors"
	>
		<div class="flex flex-col items-center justify-center pt-5 pb-6">
			<Icon icon="tabler:upload" color="#71717a" width="36" height="36" />
			<p class="my-2 text-xs text-muted-foreground sm:text-sm">
				<span class="font-semibold">Click to upload</span> or drag and drop
			</p>
			<p class="text-xs text-muted-foreground">
				{#if files && files[0]}
					{#each Array.from(files) as file}
						{file.name} ({formatFileSize(file.size)})
					{/each}
				{:else}
					<slot name="files" />
				{/if}
			</p>
		</div>
		<div class="h-0 w-0 overflow-hidden">
			<input
				bind:files
				id="dropzone-{id}"
				{name}
				type="file"
				accept={allowedExtensions}
				{required}
			/>
		</div>
	</label>
</div>
