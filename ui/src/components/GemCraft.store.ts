import { create } from "zustand";

export const enum GemType {
    Flawless = "상급 보석",
    Perfect = "최상급 보석"
}

export interface GemCraftState {
    hotKey: string;
    modKey: string;
    defaultHotKey: string;
    gems: GemType[];
    defaultGems: string[];
}

export interface GemCraftAction {
    setHotKey: (hotKey: string, modKey?: string) => void;
    setDefaultHotKey: (hotKey: string) => void;
    setGems: (gems: GemType[]) => void;
    setDefaultGems: (gems: string[]) => void;
    save: () => void;
}

export interface GemCraftStore extends GemCraftState, GemCraftAction {}

export const gemCraftStore = create<GemCraftStore>((set, get) => ({
    hotKey: "",
    modKey: "",
    defaultHotKey: "",
    gems: [],
    defaultGems: [],
    setHotKey: (hotKey, modKey) => set({ hotKey, modKey: modKey || "" }),
    setGems: (gems) => {
        set({ gems });
        let _type: string = "";
        console.log(gems);
        if (gems.length === 1) {
            if (gems[0] === GemType.Flawless) {
                _type = "flawless";
            } else if (gems[0] === GemType.Perfect) {
                _type = "perfect";
            }
        } else if (gems.length === 2) {
            _type = "both";
        }
        try {
            // @ts-ignore
            window.pywebview.api.change_gem_find_type(_type);
        } catch (e) {}
    },
    setDefaultGems: (gems) => set({ defaultGems: gems }),
    setDefaultHotKey: (hotKey) => set({ defaultHotKey: hotKey }),
    save: () => {
        const { hotKey, modKey } = get();
        try {
            // @ts-ignore
            window.pywebview.api.set_hotKey(hotKey, modKey, "gem_craft");
        } catch (e) {
            console.error(e);
        }
    }
}));
