def writer_agent(state):
    from collections import defaultdict

    # Group identical claims with their sources
    claim_to_sources = defaultdict(set)

    for claim in state['validated_claims']:
        key = claim['claim'].strip().lower()
        claim_to_sources[key].add((claim['claim'], claim['source_url']))

    lines = [f"# Research Report on '{state['topic']}'\n"]
    
    for i, (normalized_claim, claim_sources) in enumerate(claim_to_sources.items(), 1):
        # Use the first version of the original claim text
        original_claim = list(claim_sources)[0][0]
        sources = [f"[Source {j+1}]({src})" for j, (_, src) in enumerate(claim_sources)]
        lines.append(f"{i}. {original_claim} {' '.join(sources)}")

    final_report = "\n\n".join(lines)
    return {'report': final_report}
