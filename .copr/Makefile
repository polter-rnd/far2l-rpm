srpm:
	@if [ "$(notdir $(basename $(spec)))" = "far2l-tty" ]; then \
		sed -i --follow-symlinks 's/%bcond_without gui/%bcond_with gui/' "$(spec)"; \
	fi

	cp -f *.patch "$(outdir)";

	rpmbuild --define "_sourcedir $(outdir)" --define "_srcrpmdir $(outdir)" \
	         --define="_disable_source_fetch 0" -bs "$(spec)";
