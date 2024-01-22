import { create } from "zustand";

export const enum GemType {
    Flawless = "상급",
    Perfect = "최상급"
}

export interface GemCraftState {
    hotKey: string;
    modKey: string;
    gems: GemType[];
}

export interface GemCraftAction {
    setHotKey: (hotKey: string, modKey?: string) => void;
    setGems: (gems: GemType[]) => void;
    save: () => void;
}

export interface GemCraftStore extends GemCraftState, GemCraftAction {}

export const gemCraftStore = create<GemCraftStore>((set, get) => ({
    hotKey: "",
    modKey: "",
    gems: [],
    setHotKey: (hotKey, modKey) => set({ hotKey, modKey: modKey || "" }),
    setGems: (gems) => set({ gems }),
    save: () => {
        const { hotKey, modKey, gems } = get();
        localStorage.setItem("gemCraft", JSON.stringify({ hotKey, modKey, gems }));
    }
}));
