# Interview Prep — Noise, Intern Fullstack & AI Innovation

## Pitch
I build AI systems end to end across hardware and software — a wearable AI pendant with custom firmware and cloud backend, Android voice clients, and full-stack multi-model apps — and I contribute fixes back to the open-source wearable ecosystem I build on.

## Likely questions
| Question | Answer angle | Evidence anchor (repo/PR/file) |
|---|---|---|
| Walk us through Aura's architecture | Device → firmware → backend → cloud; what each layer does | aura: firmware/src/mic.cpp, backend/routers/, CASE.stl |
| How did you find the WebGL memory leak? | Symptom → profiling → backdrop-filter compositor re-blend → fix | Omi Issue #8438 → PR #8902 |
| Explain your speaker clustering approach | Offline agglomerative, cosine linkage, why offline, 52 tests | Omi PR #8919 → adopted #12471 |
| How does John handle barge-in? | Client-side Silero VAD, WebRTC data path, turn detection | John repo |
| RAG / tool calling experience? | MCP server router, memory routers, multi-provider fallback | aura backend/routers/mcp.py, voicecoder |
| On-device ML tradeoffs? | Transfer learning + augmentation vs latency under memory limits | AICTE-Google TF/ML Kit work |
| No Flutter/iOS experience? | Gap defense below; Kotlin/Compose transfers, fast pickup record | John (learned Compose for the project) |
| No Docker/CI-CD? | Gap defense below; Helm charts authored, eager on pipelines | aura K8s Helm charts |

## Gap defenses
- **Flutter/iOS/Swift/Dart:** not claimed. Framing: picked up Kotlin + Jetpack Compose specifically to ship John; cross-platform is the next learn, fundamentals (state, lifecycles) transfer.
- **Docker/CI-CD/microservices:** not claimed. Framing: authored Kubernetes Helm charts for Aura's ASR deployment; container and pipeline tooling is the gap being closed, eagerness only.
- **SQL/GraphQL:** not claimed. Framing: REST + pgvector/Supabase in production use on Aura; query-language pickup is fast.
- **Wearable sensors at Noise scale:** Aura is prototype scale, stated openly; the device-behaving gap (power, thermals, firmware OTA) is lived experience, not claimed scale.

## Questions for them
1. Which team owns on-device AI vs cloud AI for the wearable lineup — and where would an intern's prototype land first?
2. What does the path from R&D prototype to a NoiseFit-shipped feature actually look like (gates, timelines)?
3. Is there companion-app (Android/iOS) work on the intern roadmap, or mostly web + model work?
4. What sensor data (PPG, accelerometer, HR) is available to experiment with internally?
5. How is intern mentorship structured — one senior lead or rotation across AI/mobile teams?
