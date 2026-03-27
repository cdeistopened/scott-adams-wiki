import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [],
  afterBody: [
    Component.ChatWidget({
      wiki: "scott_adams",
      apiUrl: "https://api-production-4224.up.railway.app",
    }),
  ],
  footer: Component.Footer({
    links: {
      "About Scott Adams": "/about",
      "Creative Intelligence Agency": "https://creativeintel.agency",
      "Skill Stack": "https://skillstack.md",
      "GitHub": "https://github.com/cdeistopened",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ChatBanner({
      label: "Ask the Archive",
      description: "Chat with an AI that's read all 1,151 episodes",
    }),
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer({
      folderDefaultState: "open",
      filterFn: (node) => {
        // Hide episodes folder (too many - 1,151 items) and tags
        return node.slugSegment !== "tags" && node.slugSegment !== "episodes"
      },
      sortFn: (a, b) => {
        // Feature domains first, then frameworks, cases, people
        const order = ["domains", "frameworks", "cases", "people"]
        const aIdx = order.indexOf(a.slugSegment ?? "")
        const bIdx = order.indexOf(b.slugSegment ?? "")
        if (aIdx !== -1 && bIdx !== -1) return aIdx - bIdx
        if (aIdx !== -1) return -1
        if (bIdx !== -1) return 1
        return a.displayName.localeCompare(b.displayName)
      },
    }),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer({
      folderDefaultState: "open",
      filterFn: (node) => {
        return node.slugSegment !== "tags" && node.slugSegment !== "episodes"
      },
      sortFn: (a, b) => {
        const order = ["domains", "frameworks", "cases", "people"]
        const aIdx = order.indexOf(a.slugSegment ?? "")
        const bIdx = order.indexOf(b.slugSegment ?? "")
        if (aIdx !== -1 && bIdx !== -1) return aIdx - bIdx
        if (aIdx !== -1) return -1
        if (bIdx !== -1) return 1
        return a.displayName.localeCompare(b.displayName)
      },
    }),
  ],
  right: [],
}
