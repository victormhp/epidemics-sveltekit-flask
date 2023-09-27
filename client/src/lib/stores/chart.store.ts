import type { ChartActions, ChartConfig } from '../models/chart.model';
import { writable, type Writable } from 'svelte/store';
import { getContext, setContext } from 'svelte';

// Chart config
export function setChartConfig(initialConfig: ChartConfig) {
	const chart = writable<ChartConfig>(initialConfig);
	setContext('chart', chart);
}

export function getChartConfig() {
	return getContext<Writable<ChartConfig>>('chart');
}

export function updateChartConfig(currentConfig: Writable<ChartConfig>, newConfig: Partial<ChartConfig>) {
	currentConfig.update((config) => ({
		...config,
		...newConfig
	}));
}

// Chart actions
export const chartActions = writable<ChartActions>();
