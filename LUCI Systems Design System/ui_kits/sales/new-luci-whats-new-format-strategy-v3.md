# New LUCI What’s New — format strategy v3

**Revised recommendation for Jane · 17 September 2026**

**Decision status:** This memo supersedes `new-luci-whats-new-format-strategy-v2.md` for decision-making. V1 and v2 remain intact as research history.

## The answer in one sentence

Use three distinct levels: the **one-pager makes the short benefit argument**, the **Upgrade Guide + FAQ opens an optional door to deeper feature and technical detail**, and **LUCI fulfills each upgrade through a named person, a thin account plan, and a shipped laptop**.

The guide returns, but not as the public self-serve download and version hub proposed in v1. It explains. It does not distribute software, select hardware, or replace the LUCI team.

## The LUCI-shaped release path

### 1. One-pager = the short argument

The one-pager is the shared release orientation for customers, prospects, sales conversations, and PR follow-up. Its job is to make the release promise memorable:

- **Theme:** Putting the power of programming in your hands
- **Three benefit pillars:** names and arguments locked in a separate decision
- **Selected proof:** enough product evidence to make each benefit credible
- **One next action:** a guided route to see more or speak with LUCI

It should not carry feature mechanics, setup instructions, access detail, compatibility answers, or the complete technical catalog. Those belong behind the optional deeper door.

### 2. Upgrade Guide + FAQ = the optional deeper door

The guide is the maintained reference LUCI can point to when a customer or prospect wants more than the one-pager provides. It should answer four kinds of questions:

1. **What the release does:** a deeper explanation of the features under each pillar
2. **How the upgrade generally works:** what to expect before, during, and after fulfillment
3. **What common questions have one shared answer:** a practical FAQ
4. **How selected technical features work:** enough depth for an IT or A/V lead to evaluate security, identity, sessions, diagnostics, incidents, and similar subjects

The guide is not the upgrade itself. It should contain no software download, version archive, SKU chooser, or self-install path. It should not imply that reading the guide makes a customer ready to proceed without an account-specific review.

### 3. Fulfillment = human + thin account plan + laptop

The upgrade remains one-to-one:

**Customer interest or LUCI outreach → named LUCI contact → thin account-specific plan → shipped laptop → coordinated activation and support**

The thin plan carries the facts a shared guide cannot: timing, property-specific requirements, existing technology and endpoints, responsibilities, delivery, any additional hardware, and the support route. It should be brief enough to use, but specific enough that both sides know what happens next.

The shipped laptop is the fulfillment object. The guide never masquerades as a path to obtain the software.

## Recommended guide structure

Keep the guide finite and task-based rather than turning it into a documentation library.

1. **New LUCI at a glance**
   Theme, benefit pillars, and who the guide is for.

2. **What is new**
   Deeper feature explanations grouped under the approved pillars. Preserve the mapping in `new-luci-feature-list.json`.

3. **What to expect from an upgrade**
   A broad sequence: connect with LUCI, review the account, confirm the plan, receive the laptop, coordinate activation, and continue with LUCI support. Do not publish universal timing, compatibility, or interruption promises.

4. **For IT and A/V**
   Selected technical depth from the approved feature source: identity and sessions, private tunnel, scoped diagnostic capture, audit trails and incidents, endpoint management, and relevant feature mechanics.

5. **FAQ**
   Shared answers only. Route installation-specific answers to the named LUCI contact and account plan.

6. **Next step**
   Contact LUCI or continue with the person already managing the account. No download CTA.

Use a visible “last updated” date and one owner for release-fact maintenance. A future PDF may be a dated derivative, but it should not become a competing source.

## Draft FAQ starters for Jane to edit

These are starter questions, not locked public copy. Final answers should be checked against the release state, Mike’s approved feature list, and the support policy before publication.

### What is different in New LUCI?

Start with the benefit argument, then point to the approved features under each pillar. Do not answer with a flat change log.

### Can we download or install the upgrade ourselves?

No. LUCI fulfills the upgrade directly. A named LUCI contact confirms the account-specific plan, and the new software arrives on a shipped laptop.

### What happens after we decide to upgrade?

LUCI reviews the account, confirms timing and responsibilities in a short plan, ships the laptop, and coordinates activation and support.

### Will New LUCI work with our existing endpoints and technology?

That answer is account-specific. LUCI reviews the property’s current environment as part of the upgrade plan; the guide should not make a blanket compatibility promise.

### Will the upgrade interrupt current operations?

Timing and operating impact depend on the account plan. State the broad coordination process, then route the reader to the named LUCI contact for the property-specific answer.

### What can someone control from a venue panel?

An administrator scopes the panel to its assigned venue and chooses which controls are available. The panel does not expose the main LUCI application or anything outside its designated scope.

### Can we prepare a change without affecting what is currently running?

Staging lets a team build the next set while the current one continues, then apply the change on cue. A staged set can also be saved for later use.

### How are actions and incidents recorded?

Audit trails associate actions with a person and time and identify whether a person, preset, or schedule triggered them. Device incidents open when a device stops responding and close when it recovers. Any caveat about changes made outside LUCI must match the approved driver-level detail.

### How do sign-in and session controls work?

Approved methods include email, PIN, and Microsoft Entra ID. Administrators can terminate active sessions and post a site-wide message. The final answer should distinguish identity, active-session control, and floor-use PINs.

### How does the private connection work?

The approved technical explanation is one encrypted outbound connection between the on-property system and LUCI, with rotating keys and no standing inbound access to the property network. Keep implementation detail proportional to the audience.

### What happens when we need help?

The LUCI team remains part of the operation. In-product support can start from a device, incident, or error and carry relevant context and logs with the request. More control does not mean reduced support.

### What happens to support for the current version?

Do not publish a date or consequence until Jane locks the policy. Once locked, the guide may point to the current support policy, but affected customers should receive intentional direct notices and account follow-up. The policy must not be buried in this FAQ.

## Access model — controlled reference, not self-serve fulfillment

The guide should be usable by customers and prospects when LUCI points them there. “Controlled” describes the route and the content, not necessarily a login wall. The URL model remains Jane’s later decision.

### Option A — unlisted, stable web URL

LUCI shares a durable URL in email and direct conversations. The page is easy to revisit and update but is not positioned as a public upgrade center.

**Recommendation:** Start here. It creates the least friction for customers and selected prospects while keeping the context intentional.

### Option B — access-controlled customer page

Require authentication or a customer portal route. This gives tighter distribution control but adds friction and may prevent prospects from using the same deeper reference.

**Use if:** technical or account-sensitive content cannot sit at an unlisted URL.

### Option C — directly delivered, versioned PDF

Send a dated guide to each recipient. This is easy to control but creates stale copies and weakens the “one current answer” principle.

**Use as:** a derivative or procurement attachment, not the canonical source.

None of these options includes a download portal, version archive, model selector, or self-service installation path.

## The rest of the communications system

### Email routes the audience

- **Current customers:** benefit story → guide for optional depth → named contact and account-specific fulfillment
- **Prospects:** benefit story → selected guide detail when useful → webinar, overview video, or guided conversation

The sends can change context and next action without creating separate release narratives.

### Webinar or overview video demonstrates

Use one or both if useful. Their job is to show workflows, orient the audience, and answer questions. They do not replace the written guide or create a second technical source of truth.

### PR creates awareness

Keep a press release in the plan. It should carry the release benefit story and external significance, not upgrade mechanics, unsupported proof, or named-client claims without approval. Owned release and earned pickup are separate; publication is not guaranteed.

### End of support remains an intentional notice program

Once Jane locks the date and policy, affected customers should receive direct notices, account follow-up, and reminders. The guide may point to the current policy, but it is not the primary notice and must not hide the policy inside a download FAQ.

## What this architecture prevents

- The one-pager becoming a feature catalog
- The guide becoming a documentation maze
- A visitor mistaking information access for software access
- Generic guidance overriding an account-specific upgrade plan
- The webinar becoming the only durable explanation
- End-of-support policy disappearing inside release documentation
- Different channels inventing different feature claims

## Decisions still Jane’s

1. The final pillar names and benefit arguments
2. Guide access: unlisted URL, access-controlled page, or another controlled route
3. Guide location and owner
4. Webinar, overview video, or both
5. PR outlets and outreach ownership
6. End-of-support date, policy, notice timing, and consequence language
7. Final one-pager CTA and guide CTA

## Recommended lock

Lock the release architecture as:

**One-pager = short argument · Upgrade Guide + FAQ = optional deeper door · Fulfillment = named LUCI contact + thin account plan + shipped laptop**

Support that core with audience-routing email, optional demonstration, PR, and intentional end-of-support notices. Keep the guide current and useful, but never let it imply a self-serve product or an ownerless upgrade.
