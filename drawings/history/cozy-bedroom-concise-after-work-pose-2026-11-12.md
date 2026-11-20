# Cozy bedroom, concise after-work pose prompt

- **Date:** 2026-11-12 (Asia/Ho_Chi_Minh)
- **Branch:** `artwork/portrait-attempt-2026-11-10`
- **Status:** Attempt 20 recorded; generated but missed the target.
- **Builds on:** Successful scene wording in attempt 04 of [the session image prompt history](2026-11-12-image-prompts.md), with the requested cream cardigan, navy polo and explicit hand order.
- **Correct pose:** The man lies on his side with his head resting against the woman's upper chest/shoulder. She sits supported by pillows.
- **Hand placement:** Her left hand cradles his hair. On her lap, her right hand is underneath his left hand.
- **Exact authored prompt:**

> Create a tender, fully clothed comfort scene in a cozy bedroom at the end of a long day. An adult man lies on his side on the bed, visibly tired but peaceful, with his head resting gently against the upper chest and shoulder of his adult female partner. She sits comfortably upright against the pillows and headboard. Do not reverse the pose: he is resting against her.

She wears a modest cream knit cardigan over a simple high-neck top. He wears a plain dark navy polo. Keep both garments clearly visible and fully covering. Give the woman her established short dark chin-length bob and black-rimmed glasses; give the man short black hair and black-rimmed glasses.

The woman's left hand gently cradles the back of his head, fingers softly resting in his hair. Their other hands rest together on her lap, clearly visible: her right hand underneath, his left hand resting gently on top. Keep this exact order. The fingers are relaxed and distinct, not interlaced. The man's right hand rests naturally on the duvet. Do not put her hand on his chest; do not wrap his arm around her.

Show enough of both people and her lap to make the pose and hand placement unmistakable. Warm amber bedside lamp, soft ivory bedding, layered pillows, quiet evening bedroom, pink flowers and books in the background. Calm, safe, reassuring expressions. Natural, softly painted realistic illustration. No logos, no text, no extra people, no kissing, no sensual posing, no cropped hands.

- **Accuracy note:** This is the authored prompt committed before the call. The image interface may infer/normalize a hidden payload and does not expose a compiled prompt.


#### 20 result
- **Actual result:** Image generated and returned, but it repeated the same reversed close-embrace composition.
- **Observed:** The woman rests against the man, her hand is on his polo/chest, and his arm is around her. The man is not resting against the woman; her left hand is not cradling his hair; their other hands are not arranged on her lap with her right underneath his left. The short bob and black-rimmed glasses are absent, and the navy polo has a visible logo.
- **Image tool ID:** `447877e8-a1cc-4f8a-8cc9-393fae340803`.
- **Local artifact:** `/mnt/data/a_warm_cozy_romantic_bedroom_illustration_photor.png`.
- **File facts:** PNG, 1312 × 1199 pixels, 2,632,029 bytes; SHA-256 `b7aa01f06e7b4e3c71d602bc6c7e5367cd74f665f38e61caca2decb01c3fe61b`.
- **Classification:** Generated, but did not match the defining pose or hand placement. Not a successful match.
- **Learning:** The generation interface repeatedly infers the same woman-against-man composition even when the authored prompt explicitly assigns the opposite role and exact hands. Do not describe this as a prompt-compliance success. A future attempt would need a generation/edit workflow that accepts and follows an explicit reference image and prompt controls rather than relying on context inference alone.
